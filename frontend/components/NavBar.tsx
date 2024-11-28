// frontend/components/NavBar.tsx
import { useState } from "react";
import Link from "next/link";

const NavBar = () => {
  const [user, setUser] = useState(null); // This will hold user state after login

  const handleLogout = () => {
    setUser(null); // Clear the user state to simulate logout
    // Optionally, also clear sessionStorage or localStorage here if you are storing tokens
  };

  return (
    <nav className="bg-gray-800 text-white p-4">
      <div className="container mx-auto flex justify-between items-center">
        <Link href="/" className="text-2xl font-bold">
          Slack Clone
        </Link>
        
        {/* Show links depending on whether the user is logged in */}
        <div>
          {user ? (
            <>
              <Link href="/dashboard" className="mr-4">Dashboard</Link>
              <button onClick={handleLogout} className="bg-red-500 text-white px-4 py-2 rounded">Logout</button>
            </>
          ) : (
            <>
              <Link href="/login" className="mr-4">Login</Link>
              <Link href="/demo" className="mr-4">Demo</Link>
            </>
          )}
        </div>
      </div>
    </nav>
  );
};

export default NavBar;
