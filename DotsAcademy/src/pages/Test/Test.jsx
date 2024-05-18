import React, { useState } from "react";
import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";
import styles from "./Test.module.scss";
const Test = () => {
  const [videoLink, setVideoLink] = useState("");
  const [pdfFile, setPdfFile] = useState(null);

  const handleVideoLinkChange = (e) => {
    setVideoLink(e.target.value);
  };

  const handlePdfFileChange = (e) => {
    setPdfFile(e.target.files[0]); // Get the first selected file
  };

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append("videoLink", videoLink);
    formData.append("pdfFile", pdfFile);

    try {
      const response = await axios.post("/api/create-test", formData);
      // Handle success (e.g., show a confirmation message, redirect)
    } catch (error) {
      console.error("Error creating test:", error);
      // Handle errors (e.g., show an error message to the user)
    }
  };
  return (
    <div>
      <Navbar />
      <div className={styles.container}>
        <h2>
          Try it yourself by creating a test using our artificial intelligence
        </h2>
        <div className={styles.wrapper_input}>
          <div className={styles.inputGroup}>
            <label htmlFor="videoLink">Upload Video Link:</label>
            <input
              type="text"
              id="videoLink"
              value={videoLink}
              onChange={handleVideoLinkChange}
            />
          </div>

          <div className={styles.inputGroup}>
            <label htmlFor="pdfFile">Select PDF File:</label>
            <input
              type="file"
              id="pdfFile"
              accept=".pdf"
              onChange={handlePdfFileChange}
            />
          </div>

          <p className={styles.info}>
            Questions in the system are created using the given materials!!!
          </p>

          <button className={styles.doneButton} onClick={handleSubmit}>
            Done
          </button>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default Test;
