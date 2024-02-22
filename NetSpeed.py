import speedtest
import time

#st = speedtest.Speedtest()
#st.download()

#print("Download Speed: {:.2f} Mbps".format(st.results.download/ 1024/1024))


# Create speedtest object
st = speedtest.Speedtest()

def get_speed():
    # Perform speed test
    download_speed = st.download() / 1024 / 1024  # Convert to MBps
    upload_speed = st.upload() / 1024 / 1024  # Convert to MBps

    return download_speed, upload_speed

def main():
    while True:
        download_speed, upload_speed = get_speed()
        print(f"Download Speed: {download_speed:.2f} MBps")
        print(f"Upload Speed: {upload_speed:.2f} MBps")
        print("-" * 20)

        # Wait for some time before next test
        time.sleep(5)

if __name__ == "__main__":
    main()






