A simple python GUI for appending multiple text files into an LLM chat for work to be done on them. Files are selected, proccessed and then either outputted to a file, or copied to a clipboard. Particularly useful for updating the original prompt with code changes made later on.
 Written entirely by Claude 3.5 Sonnet.

![App Image](https://private-user-images.githubusercontent.com/88689980/358933097-5c1bea4f-def5-450a-b457-51ffd50246e6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjQwMTIwMzQsIm5iZiI6MTcyNDAxMTczNCwicGF0aCI6Ii84ODY4OTk4MC8zNTg5MzMwOTctNWMxYmVhNGYtZGVmNS00NTBhLWI0NTctNTFmZmQ1MDI0NmU2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MTglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODE4VDIwMDg1NFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWVlMGVmNWQxN2RkM2RhOGQ5OTMyZGNjZDA2MzQ5ZmU5MjI4NTEzOTIwZWQ5NzVmODgxZmMxMTQyODQ0ZjY1ZTcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.v5RuOQtrRcX-QXxdIX15GEQLFdYPpX6_gF3I395VR3U
)

Each files contents will be surrounded by markdown code blocks, with the filename appended at the front surrounded by markdown, they'll all then be either added together in one file, or pasted all together.
