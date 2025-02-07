// const fileInput = document.getElementById('file-upload'); 
// const fileNameDisplay = document.getElementById('file-name');

// // Display the selected file name
// fileInput.addEventListener('change', (event) => {
//     const file = event.target.files[0];
//     fileNameDisplay.textContent = file ? file.name : 'No file chosen';
// });

// // Submit the form data to the backend
// async function uploadResume() {
//     const file = fileInput.files[0];

//     if (!file) {
//         alert("Please choose a file first!");
//         return;
//     }

//     const formData = new FormData();
//     formData.append('resume', file);
//     formData.append('job_description', document.getElementById('job-description').value);

//     try {
//         const response = await fetch('/upload', {
//             method: 'POST',
//             body: formData
//         });

//         const data = await response.json();

//         if (data.questions) {
//             displayQuestions(data.questions);
//         }
//     } catch (error) {
//         console.error('Error uploading file:', error);
//     }
// }

// // Render the interview questions on the page
// function displayQuestions(questions) {
//     const questionsSection = document.getElementById('questions');
//     questionsSection.innerHTML = '<h2>Generated Interview Questions:</h2>';

//     const ul = document.createElement('ul');
//     questions.forEach(question => {
//         const li = document.createElement('li');
//         li.textContent = question;
//         ul.appendChild(li);
//     });

//     questionsSection.appendChild(ul);
// }

// const fileInput = document.getElementById('file-upload'); 
// const fileNameDisplay = document.getElementById('file-name');

// fileInput.addEventListener('change', (event) => {
//     const file = event.target.files[0];
//     fileNameDisplay.textContent = file ? file.name : 'No file chosen';
// });

// async function uploadResume() {
//     const file = fileInput.files[0];

//     if (!file) {
//         alert("Please choose a file first!");
//         return;
//     }

//     const formData = new FormData();
//     formData.append('resume', file);
//     formData.append('job_description', document.getElementById('job-description').value);

//     try {
//         const response = await fetch('/analyze', {
//             method: 'POST',
//             body: formData
//         });

//         const data = await response.json();

//         if (data.questions) {
//             displayQuestions(data.questions);
//         }
//     } catch (error) {
//         console.error('Error uploading file:', error);
//     }
// }

// function displayQuestions(questions) {
//     const questionsSection = document.getElementById('questions');
//     questionsSection.innerHTML = '<h2>Generated Interview Questions:</h2>';
//     const ul = document.createElement('ul');
//     questions.forEach(question => {
//         const li = document.createElement('li');
//         li.textContent = question;
//         ul.appendChild(li);
//     });
//     questionsSection.appendChild(ul);
// }

const fileInput = document.getElementById('file-upload');
const fileNameDisplay = document.getElementById('file-name');

// Display the selected file name
fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    fileNameDisplay.textContent = file ? file.name : 'No file chosen';
});

// Submit the form data to the backend and handle the response
async function uploadResume() {
    const file = fileInput.files[0];

    if (!file) {
        alert("Please choose a file first!");
        return;
    }

    const formData = new FormData();
    formData.append('resume', file);
    formData.append('job_description', document.getElementById('job-description').value);

    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const data = await response.json();

            if (data.questions) {
                displayQuestions(data.questions);
            } else {
                alert('No questions generated.');
            }
        } else {
            alert('Error analyzing resume. Please try again.');
        }
    } catch (error) {
        console.error('Error uploading file:', error);
    }
}

// Render the interview questions on the page
function displayQuestions(questions) {
    const questionsSection = document.getElementById('questions');
    questionsSection.innerHTML = '<h2>Generated Interview Questions:</h2>';

    const ul = document.createElement('ul');
    questions.forEach(question => {
        const li = document.createElement('li');
        li.textContent = question;
        ul.appendChild(li);
    });

    questionsSection.appendChild(ul);
}
