import React, { Fragment, useState } from "react";
import axios from "axios";

const FileUpload = (props) => {
  const [file, setFile] = useState();
  const [filename, setFilename] = useState();
  const [uploadedFile, setUploadedFile] = useState({});

  const fileHandler = (e) => {
    setFile(e.target.files[0]);
    setFilename(e.target.files[0].name);
  };

  const submitHandler = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://localhost:5000/upload", formData, {
        headers: { "Contenet-Type": "multipart/form-data" },
      });

      const { fileName, filePath } = res.data;
        setUploadedFile({ fileName, filePath });
        console.log(`Filename ${fileName}`);
      console.log(filePath);
    } catch (err) {
      if (err.response.status === 500) {
        console.log("There was a problem with the server");
      } else {
        console.log(err.response.data.msg);
      }
    }
  };

  return (
    <Fragment>
      <form onSubmit={submitHandler}>
        <div className="mb-3">
          <label htmlFor="formFile" className="form-label">
            {props.label}
          </label>
          <input
            className="form-control"
            type="file"
            id="formFile"
            onChange={fileHandler}
          />
        </div>
        <div className="d-grid gap-2">
          <input type="submit" value="Upload" className="btn btn-dark mt-4" />
        </div>
          </form>
      { uploadedFile && <div className="row">
        <div className="col-md-6 m-auto">
          <h3 className="text-center"> { uploadedFile.fileName }</h3>
          <img style={{width: "100%"}} src={process.env.PUBLIC_URL + uploadedFile.filePath} alt={uploadedFile.fileName}></img>
        </div>
      </div> }
    </Fragment>
  );
};

export default FileUpload;
