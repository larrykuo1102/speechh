import azure.cognitiveservices.speech as speechsdk
speech_key, service_region = "29ce9077f3c54ab9811736fd9b8f7b76", "japaneast"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)


audio_input = speechsdk.AudioConfig(filename="/narration.wav")
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
print("Recognizing first result...")

result = speech_recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))