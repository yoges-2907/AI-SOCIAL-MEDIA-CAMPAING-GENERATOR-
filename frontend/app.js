const generateBtn = document.getElementById('generateBtn');
const copyBtn = document.getElementById('copyBtn');
const downloadBtn = document.getElementById('downloadBtn');

const captionDiv = document.getElementById('caption');
const previewImg = document.getElementById('preview');
const historyList = document.getElementById('historyList');

const API_URL = 'http://127.0.0.1:8000';

generateBtn.addEventListener('click', generatePost);
copyBtn.addEventListener('click', copyCaption);
downloadBtn.addEventListener('click', downloadImage);

async function generatePost() {
  const prompt = document.getElementById('prompt').value.trim();
  const platform = document.getElementById('platform').value;
  const tone = document.getElementById('tone').value;

  if (!prompt) {
    alert('Please enter a prompt');
    return;
  }

  generateBtn.disabled = true;
  generateBtn.textContent = 'Generating...';

  captionDiv.textContent = 'Generating caption...';
  previewImg.src = '';
  downloadBtn.disabled = true;

  try {
    const response = await fetch(`${API_URL}/generate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        prompt,
        platform,
        tone
      })
    });

    if (!response.ok) {
      throw new Error('Server error');
    }

    const data = await response.json();

    captionDiv.textContent = data.caption || 'No caption generated';

    if (data.image_url) {
      previewImg.src = `${API_URL}${data.image_url}`;
      downloadBtn.disabled = false;
      loadHistory();  // Refresh history after generating a new post
    }

  } catch (error) {
    console.error(error);
    captionDiv.textContent = 'Failed to generate post. Make sure the FastAPI server is running.';
  } finally {
    generateBtn.disabled = false;
    generateBtn.textContent = 'Generate Post';
  }
}

function copyCaption() {
  const text = captionDiv.textContent;

  navigator.clipboard.writeText(text)
    .then(() => {
      copyBtn.textContent = 'Copied';
      setTimeout(() => {
        copyBtn.textContent = 'Copy Caption';
      }, 2000);
    });
}

function downloadImage() {
  if (!previewImg.src) return;

  const link = document.createElement('a');
  link.href = previewImg.src;
  link.download = 'ai-social-post.png';
  link.click();
}

async function loadHistory() {
  try { 
    const response = await fetch(`${API_URL}/history`); 
    const data = await response.json(); 
    if (!data.length) { historyList.innerHTML = '<p>No history yet</p>'; 
      return; 
    }

    historyList.innerHTML = data
    .slice(0, 5)
    .map(item =>  `
      <div class="history-item">
        <h3>${item.platform.toUpperCase()} • ${item.tone}</h3> 
        <p>${item.prompt}</p> 
      <div class="history-meta">${item.created_at}</div> 
      </div> 
      `) 
      .join(''); 
    } 
    catch (error) { 
      historyList.innerHTML = '<p>Failed to load history</p>'; 
    } 
  } 
  
  loadHistory();