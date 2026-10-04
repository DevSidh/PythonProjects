import speedtest
st = speedtest.Speedtest()

download = st.download() / 1_000_000
upload = st.upload() / 1_000_000
ping = st.results.ping

print(f"Downloading Speed: {download}")
print(f"Uploading Speed: {upload}")
print(f"ping: {ping}")