mkdir /run/shm/mjpg

# repeatedly take picutres and store to tmpfs
# may need to compensate for the orientation of the camera
# -hf, -hflip - horizontal flip
# -vf, -vflip - vertical flip
# -rot, --rotation - Set image rotation (0-359)
raspistill -t 999999 -tl 500 -o /run/shm/mjpg/test.jpg -n -w 640 -h 480 -rot 90&

# send the stream
/usr/bin/mjpg_streamer -i '/usr/lib/input_file.so -f /run/shm/mjpg -d 600 -n test.jpg' -o '/usr/lib/output_http.so -p 8090 -w ./www'
