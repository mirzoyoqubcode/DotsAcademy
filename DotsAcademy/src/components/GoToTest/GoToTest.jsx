import React from "react";
import styles from "./GoToTest.module.scss";
import { Link } from "react-router-dom";

const GoToTest = () => {
  return (
    <div className={styles.test_section}>
      <p>
        Through our system, you can find out your knowledge by creating a test
        even in the case when you upload the knowledge you received from
        external factors
      </p>
      <Link to={"/maketest"} className={styles.btn_test_link}>
        <button className={styles.btn_test}>Make test</button>
      </Link>
    </div>
  );
};

export default GoToTest;
