import React from "react";
import { Link } from "react-router-dom";
import logo from "../../assets/logo.jpg"; // Ensure path is correct
import "./Nav.css";

const Nav = () => {
  return (
    <nav className="navbar">
      <div className="nav-links">
        <Link to="/">Home</Link>
        <Link to="/menu">Menu</Link>
        <Link to="/about">About</Link>
        <Link to="/contact">Contact</Link>
      </div>
      <div className="nav-logo">
        <img src={logo} alt="Logo" />
      </div>
    </nav>
  );
};

export default Nav;
