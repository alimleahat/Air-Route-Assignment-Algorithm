import math

def calc_stats(data):
    # Calculate mean
    total = sum(data)
    mean = total / len(data)
    
    # Calculate standard deviation
    sum_squared_diff = 0
    for x in data:
        diff = x - mean
        sum_squared_diff += diff * diff
    variance = sum_squared_diff / len(data)
    std = math.sqrt(variance)
    
    # Calculate skewness
    if std > 0:
        sum_cubed_diff = 0
        for x in data:
            sum_cubed_diff += (x - mean)**3
        skew = sum_cubed_diff / len(data) / (std**3)
    else:
        skew = 0
        
    return mean, std, skew


def resample_monthly(timestamps, values):
    # Group data by month
    monthly_data = {}
    for i in range(len(timestamps)):
        month_key = timestamps[i][:7]  # Get 'YYYY-MM' part
        if month_key not in monthly_data:
            monthly_data[month_key] = 0
        monthly_data[month_key] += values[i]
    
    # Sort and separate keys and values
    sorted_months = sorted(monthly_data.keys())
    monthly_values = [monthly_data[m] for m in sorted_months]
        
    return sorted_months, monthly_values


def resample_quarterly(periods, totals):
    # Group by quarters
    quarterly_data = {}
    for i in range(len(periods)):
        year, month = periods[i].split('-')
        month = int(month)
        quarter = (month - 1) // 3 + 1  # Calculate quarter number
        quarter_key = f"{year}-Q{quarter}"
        
        if quarter_key not in quarterly_data:
            quarterly_data[quarter_key] = 0
        quarterly_data[quarter_key] += totals[i]
    
    # Sort and separate keys and values
    sorted_quarters = sorted(quarterly_data.keys())
    quarterly_values = [quarterly_data[q] for q in sorted_quarters]
        
    return sorted_quarters, quarterly_values


def resample_annual(periods, totals):
    # Group by year
    yearly_data = {}
    for i in range(len(periods)):
        year = periods[i][:4]  # First 4 characters (the year)
        if year not in yearly_data:
            yearly_data[year] = 0
        yearly_data[year] += totals[i]
    
    # Sort and separate keys and values
    sorted_years = sorted(yearly_data.keys())
    yearly_values = [yearly_data[y] for y in sorted_years]
        
    return sorted_years, yearly_values