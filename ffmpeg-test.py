import ffmpeg
(
    ffmpeg
    .input('video1.mp4', ss='00:01:00')
    .filter('scale', 320, -1)
    .output('out.png', vframes=1)
    .run()
)