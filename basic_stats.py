from utils.helper import read_csv_files_in_directory, display_top_items

df = read_csv_files_in_directory("data", "cache", "network_analysis_data.pkl")

# The total number of network flows is the number of rows in the DataFrame
print("Total number of network flows:", len(df))

# Top 5 most used protocols
top_protocols = df['protocolName'].value_counts().head(5)
display_top_items("Top 5 most used protocols", top_protocols)

# Top 10 source IPs
top_sources = df['source'].value_counts().head(10)
display_top_items("Top 10 most active Source IPs", top_sources)

# Top 10 destination IPs
top_destinations = df['destination'].value_counts().head(10)
display_top_items("Top 10 most active Destination IPs", top_destinations)

# Average packet size = total bytes / total packets
total_bytes = df['totalSourceBytes'].sum() + df['totalDestinationBytes'].sum()
total_packets = df['totalSourcePackets'].sum(
) + df['totalDestinationPackets'].sum()
if total_packets > 0:
    avg_packet_size = total_bytes / total_packets
    print(f"\nAverage packet size: {avg_packet_size:.2f} bytes")
else:
    print("\nNo packets found to compute average.")

# Create a new column for source-destination pairs
# Count occurrences of each pair
df['src_dst_pair'] = df['source'] + " → " + df['destination']
most_common_sd_pair = df['src_dst_pair'].value_counts().head(1)
display_top_items("Most common source-destination pair", most_common_sd_pair)
