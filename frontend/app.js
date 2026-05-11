let currentGeneratedCode = "";

async function generateCode() {

    try {

        const prompt = document.getElementById('prompt').value;
        const btn = document.getElementById('genBtn');

        btn.innerText = "Generating...";

        console.log("BUTTON CLICKED");

        // CALL BACKEND
        const response = await fetch('https://coding-buddy-backend-pjta.onrender.com/api/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt })
        });

        console.log("Response received");

        const data = await response.json();

        console.log(data);

        // SHOW FILE LIST
        const fileList = document.getElementById('file-list');

        if (fileList) {

            fileList.innerHTML = "";

            data.files.forEach(file => {
                fileList.innerHTML += `<div>${file}</div>`;
            });

        }

        // UPDATE PREVIEW
        const iframe = document.getElementById('preview-frame');

        iframe.src = data.preview_url;

        // ENABLE DOWNLOAD
        const downBtn = document.getElementById('downBtn');

        downBtn.disabled = false;

        downBtn.onclick = () => {
            window.location.href = "https://coding-buddy-backend-pjta.onrender.com/download";
        };

        btn.innerText = "Generate & Preview";

    } catch(err) {

        console.error(err);

    }
}
function downloadCode() {

    window.open(
        'https://coding-buddy-backend-pjta.onrender.com/download',
        '_blank'
    );

}
