from flask import Flask, request, send_file
from gtts import gTTS
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import os

app = Flask(__name__)

VIDEO_FOLDER = "/app/videos"
OUTPUT_FOLDER = "/app/output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/create_video", methods=["POST"])
def create_video():
    data = request.form
    text = data.get("text")
    background_video = data.get("background_video")

    if not text or not background_video:
        return {"error": "Missing 'text' or 'background_video'"}, 400

    video_path = os.path.join(VIDEO_FOLDER, background_video)
    if not os.path.exists(video_path):
        return {"error": "Background video not found"}, 404

    # Generate TTS
    tts = gTTS(text=text, lang="en")
    audio_path = os.path.join(OUTPUT_FOLDER, "tts.mp3")
    tts.save(audio_path)

    # Load video and audio
    clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)
    clip = clip.set_audio(audio_clip)

    # Add text overlay
    txt_clip = TextClip(text, fontsize=50, color='white', method='caption', size=clip.size)
    txt_clip = txt_clip.set_duration(clip.duration).set_position('center')

    final_clip = CompositeVideoClip([clip, txt_clip])
    output_path = os.path.join(OUTPUT_FOLDER, "final_video.mp4")
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
