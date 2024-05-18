import React from "react";
import styles from "./Header.module.scss";
import black from "../../assets/black.svg";
import purple from "../../assets/purple.svg";
const Header = () => {
  return (
    <div className={styles.wrapper_header}>
      <div className={styles.header_first}>
        <p>
          On our web platform for online courses, you will have the opportunity
          to take tests divided into difficulty levels after mastering the
          lessons. This feature allows for a comprehensive assessment of your
          understanding and progress.
        </p>
        <img src={black} alt="" />
      </div>
      <div className={styles.header_second}>
        <img src={purple} alt="" />
        <p>
          Learning flow rates, mark tests based on their difficulty levels, and
          collect points, which you can then monitor over time
        </p>
      </div>
      <div className={styles.videos_youtube}></div>
    </div>
  );
};

export default Header;
