import pandas as pd

# Brief info found at
# https://netbeez.net/blog/http-transaction-timing-breakdown-with-curl/
#
# lookup: The time, in seconds, it took from the start until the name resolving was completed.
# connect: The time, in seconds, it took from the start until the TCP connect to the remote host (or proxy) was completed.
# appconnect: The time, in seconds, it took from the start until the SSL/SSH/etc connect/handshake to the remote host was completed. (Added in 7.19.0)
# pretransfer: The time, in seconds, it took from the start until the file transfer was just about to begin. This includes all pre-transfer commands and negotiations that are specific to the particular protocol(s) involved.
# redirect: The time, in seconds, it took for all redirection steps include name lookup, connect, pretransfer and transfer before the final transaction was started. time_redirect shows the complete execution time for multiple redirections. (Added in 7.12.3)
# starttransfer: The time, in seconds, it took from the start until the first byte was just about to be transferred. This includes time_pretransfer and also the time the server needed to calculate the result.
# total: The total time, in seconds, that the full operation lasted. The time will be displayed with millisecond resolution.

columns = [ 
    "time_namelookup", "time_connect", "time_appconnect",
    "time_pretransfer", "time_redirect", "time_total"
]

df = pd.read_csv('output.csv', names=columns) 

df = df.drop(columns=['time_redirect', 'time_appconnect'])

# print("Data")
print(df)

print("\nAverage of Matcies")
print(df.mean())

print("\nMin")
print(df.min())

print("\nMax")
print(df.max())