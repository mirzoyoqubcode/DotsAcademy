import { Route, Routes } from "react-router-dom";
import "./App.css";
import MainPage from "./pages/MainPage";
import Test from "./pages/Test/Test";

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/maketest" element={<Test />} />
      </Routes>
    </>
  );
}

export default App;
