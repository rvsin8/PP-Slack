import { useEffect, useState } from "react";
import { fetchData } from "../utils/api";
import Link from "next/link";

// Define the type for a direct message
type DirectMessage = {
  id: number;
  content: string;
};

const DMList = () => {
  const [directMessages, setDirectMessages] = useState<DirectMessage[]>([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchDMs = async () => {
      try {
        const data = await fetchData("/direct_message"); // Ensure the endpoint is correct
        if (data && Array.isArray(data.directMessages)) {
          setDirectMessages(data.directMessages);
        } else {
          setError("No direct messages found.");
        }
      } catch (err) {
        setError("Failed to load direct messages.");
      }
    };
    fetchDMs();
  }, []);

  return (
    <div className="bg-gray-900 text-white p-4 rounded-md">
      <h2 className="text-xl mb-4">Direct Messages</h2>
      {error && <p className="text-red-500">{error}</p>}
      <ul>
        {directMessages.length > 0 ? (
          directMessages.map((dm) => (
            <li key={dm.id} className="mb-2">
              <Link href={`/direct_message/${dm.id}`} className="text-blue-500 hover:underline">
                {dm.content}
              </Link>
            </li>
          ))
        ) : (
          <li>No direct messages available.</li>
        )}
      </ul>
    </div>
  );
};

export default DMList;
