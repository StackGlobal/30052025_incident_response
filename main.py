import csv
from collections import Counter

def analyze_events(csv_file_path):
    # Initialize counters
    non_access_denied_count = 0
    total_count = 0
    event_source_counter = Counter()
    event_name_counter = Counter()
    
    with open(csv_file_path, 'r') as file:
        # Create CSV reader with DictReader to access columns by name
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            total_count += 1
            # Check if the event is not AccessDenied
            if row['Error code'] != 'AccessDenied':
                non_access_denied_count += 1
                # Count by event source and event name
                event_source_counter[row['Event source']] += 1
                event_name_counter[row['Event name']] += 1
    
    # Print results
    print(f"\nTotal events without AccessDenied error: {non_access_denied_count}")
    print(f"Total events: {total_count}")
    
    print("\nEvents by Event Source:")
    for source, count in event_source_counter.most_common():
        print(f"{source}: {count}")
    
    print("\nEvents by Event Name:")
    for name, count in event_name_counter.most_common():
        print(f"{name}: {count}")

if __name__ == "__main__":
    # Replace 'events.csv' with your actual CSV file path
    analyze_events('./event_history.csv')
