import subprocess
import time
import os
import signal

# Run the service corresponding to the user_app
def run_user_service():
    return subprocess.Popen(["python", "E:/olxa/version_2_social_media_app/version_2/social_media_app/user_app/app.py"])

# Run the service corresponding to the post_app
def run_post_service():
    return subprocess.Popen(["python", "E:/olxa/version_2_social_media_app/version_2/social_media_app/post_app/app.py"])

if __name__ == '__main__':
    # Start both services
    user_process = run_user_service()
    post_process = run_post_service()

    # Graceful termination of the two subprocesses
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nTerminating both the processes. Alvida!")
        user_process.terminate()  # Gracefully terminate the user_app process
        post_process.terminate()  # Gracefully terminate the post_app process
        user_process.wait()       # Wait for termination
        post_process.wait()
