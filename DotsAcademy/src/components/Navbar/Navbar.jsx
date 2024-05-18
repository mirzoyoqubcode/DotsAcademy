import React, { useState } from "react";
import styles from "./Navbar.module.scss";
import logo from "../../assets/logo.png";
import { Link } from "react-router-dom";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
const Navbar = () => {
  return (
    <div className={styles.wrapper_navbar}>
      <Link to={"/"}>
        <div className={styles.logo}>
          <img src={logo} alt="" />
        </div>
      </Link>

      <Link className={styles.link_navbar} to={"/categories"}>
        Categories
      </Link>
      <Box
        component="form"
        noValidate
        autoComplete="off"
        className={styles.input_wrapper}
      >
        <TextField
          label="Search for anything..."
          sx={{ width: "500px" }}
          className={styles.input_search}
        />
      </Box>
      <Link className={styles.link_navbar} to={"/business"}>
        Dots Bussiness
      </Link>
      <Link className={styles.link_navbar} to={"/teach"}>
        Teach on Dots
      </Link>
      <div className={styles.nav_buttons}>
        <Button variant="contained" className={styles.btn_nav_login}>
          Log in
        </Button>
        <Button variant="outlined" className={styles.btn_nav_signup}>
          Sign up
        </Button>
      </div>
    </div>
  );
};

export default Navbar;
