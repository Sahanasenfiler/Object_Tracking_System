document.getElementById('process-btn').addEventListener('click', async () => {
    const inputType = document.getElementById('input-type').value;
    const model = document.getElementById('model').value;
    const fileInput = document.getElementById('file');
    const outputDiv = document.getElementById('output');
  
    // Validate that a file is selected
    if (!fileInput.files.length) {
      outputDiv.textContent = 'Please select a file to process.';
      return;
    }
  
    // Prepare form data
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    formData.append('input_type', inputType);
    formData.append('model', model);
  
    try {
      // Send the request to the backend
      const response = await fetch('http://127.0.0.1:5000/process', {
        method: 'POST',
        body: formData,
      });
  
      // Parse and display the response
      const result = await response.json();
      outputDiv.textContent = `Output: ${result.message}`;
    } catch (error) {
      console.error(error);
      outputDiv.textContent = 'An error occurred while processing.';
    }
  });
  