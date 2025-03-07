import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Nav from "./components/Nav";
import Home from "./components/Home";
import './App.css';

function App() {
  return (
    <Router>
      <div className="APP">
        <Nav />
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
