import React from "react";
import styles from "./HeaderCourseVideo.module.scss";
const HeaderCourseVideo = () => {
  return (
    <div className={styles.section_video}>
      <div className={styles.video_wrapper}>
        <article>
          <iframe
            width="560"
            height="315"
            src="https://www.youtube.com/embed/8IogxPUrW7k?si=ZPxQqGv-fT6XhdN2&amp;start=1"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerpolicy="strict-origin-when-cross-origin"
            allowfullscreen
          ></iframe>
        </article>
        <article>
          <iframe
            width="560"
            height="315"
            src="https://www.youtube.com/embed/F8M6MxypjEo?si=drKc6Wtj7ndT7WDB&amp;start=2"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerpolicy="strict-origin-when-cross-origin"
            allowfullscreen
          ></iframe>
        </article>
        <article>
          <iframe
            width="560"
            height="315"
            src="https://www.youtube.com/embed/ehCrFcFxfVo?si=K_azYOPmj36gsnqq&amp;start=4"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerpolicy="strict-origin-when-cross-origin"
            allowfullscreen
          ></iframe>
        </article>
        <article>
          <iframe
            width="560"
            height="315"
            src="https://www.youtube.com/embed/IaUmrzUPU1k?si=3TO2qLx4OIXRViBc&amp;start=1"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerpolicy="strict-origin-when-cross-origin"
            allowfullscreen
          ></iframe>
        </article>
        <article>
          <iframe
            width="560"
            height="315"
            src="https://www.youtube.com/embed/IaUmrzUPU1k?si=tN1bVoG_wREzzUew&amp;start=4"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerpolicy="strict-origin-when-cross-origin"
            allowfullscreen
          ></iframe>
        </article>
      </div>
      <button className={styles.btn_video}>Starting the course</button>
    </div>
  );
};

export default HeaderCourseVideo;
