import React, { useEffect, useState } from 'react';
import './UploadFile.css';
import axios from 'axios';


function FileUpload() {
    const [files, setFiles] = useState([]);
    const [personalSkill, setPersonalSkill] = useState({});
    
    const handleFileChange = (event) => {
        const newFiles = Array.from(event.target.files); // Convert FileList to array
        setFiles([...files, ...newFiles]);
      };
    
    const handleRemoveFile = (index) => {
      const updatedFiles = [...files];
      updatedFiles.splice(index, 1);
      setFiles(updatedFiles);
    };


    const handleSubmit = (event) => {
        event.preventDefault();
    const formData = new FormData();
  files.forEach((file) => {
    formData.append('files', file);
  });

  // Send the file upload request using Axios
  axios.post('http://localhost:5000/upload', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  })
    .then((response) => {
      console.log(response.data);
      setPersonalSkill(response.data);
    })
    .catch((error) => {
      console.error('There was a problem with the request:', error);
    });
};




    useEffect(()=>{
    console.log(files);
    },[files])
   
  
    return (
      <div className="file-upload-container">
        <h2>Multiple File Upload</h2>
        <form onSubmit={handleSubmit} className="file-upload-form">
          <div className="file-input">
            <label htmlFor="fileUpload">Choose Files to Upload:</label>
            <input type="file" id="fileUpload" name="files" accept=".pdf,.doc,.docx,.xlsx,.xls,image/*,audio/*" multiple onChange={handleFileChange} />
          </div>
          <div className="uploaded-files">
            {files && files.map((file, index) => (
              <div key={index} className="uploaded-file">
                <span>{file.name}</span>
                <button type="button" onClick={() => handleRemoveFile(index)}>Remove</button>
              </div>
            ))}
          </div>
          <button type="submit">Upload Files</button>
        </form>
        <div className="personal-skill">
          <h3>Personal Skills:</h3>
          <ul>
              {Object.entries(personalSkill).map(([filename, skills], index) => (
                  <li key={index}>
                      <strong>{filename}:</strong>
                      <ul>
                          {Array.isArray(skills) ? (
                              skills.map((skill, idx) => (
                                  <li key={idx}>{skill}</li>
                              ))
                          ) : (
                              <li>{skills}</li>
                          )}
                      </ul>
                  </li>
              ))}
          </ul>
      </div>
      </div>
    );
  }
  
  export default FileUpload;
