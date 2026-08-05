import os, re , urllib.parse, urllib.request //package
from flask import Flask, request, jsonify,render_template_string, abort //package
app =Flask(_name_) //variables
HTML="""
<!DOCTYPE html>
<html>
<head>
<style>
*{}
body{}
.container{}
h2{}
button{}
button:hover{}
#status{}
</style>
</head>
<body>
<div class="container">
<h2> 🎤 Voice Agent</h2>
<button onclick="start()">Speak</button>
<p id="status"></p>
</div>
<script>
const SR= window.SpeechRecoginition||window.webkitSpeechRecognition,
s=document.getElementById("status");

async function send(cmd){
let r=await fetch("/agent",(method:"POST",headers:{"Content-Type":"application/json"},
body:JSON.stringify({text_command:cmd})});
let d=await r.json();
if(d.error)return s.innerText=d.error;
s.innerText="Opening..";
window.open(d.url,"_blank");
}

function start(){
if(!SR)return alert("Use Chrome/Edge");
let rec=new SR();
rec.lang="en-US";
rec.onresult=e=>send(e.result[0][0].transcript);
rec.onerror=e=>s.innerText=e.error;
rec.start();
}
<\/script>
</body>
</html>


