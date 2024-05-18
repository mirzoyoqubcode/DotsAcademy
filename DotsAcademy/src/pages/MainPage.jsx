import React from "react";
import Navbar from "../components/Navbar/Navbar";
import Header from "../components/Header/Header";
import HeaderCourseVideo from "../components/HeaderCourseVideo/HeaderCourseVideo";
import GoToTest from "../components/GoToTest/GoToTest";
import Footer from "../components/Footer/Footer";

const MainPage = () => {
  return (
    <div>
      <Navbar />
      <Header />
      <HeaderCourseVideo />
      <GoToTest />
      <Footer />
    </div>
  );
};

export default MainPage;
