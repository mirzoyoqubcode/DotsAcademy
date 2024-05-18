import React from "react";
import styles from "./Footer.module.scss";
const Footer = () => {
  return (
    <div className={styles.footer_section}>
      <p>
        © By <span>Dots</span> team
      </p>
    </div>
  );
};

export default Footer;
