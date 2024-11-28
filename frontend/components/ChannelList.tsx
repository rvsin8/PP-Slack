import { useEffect, useState } from "react";
import { fetchData } from "../utils/api";
import Link from "next/link";

// Define the type for a channel
type Channel = {
  id: number;
  name: string;
  description: string;
};

const ChannelList = () => {
  const [channels, setChannels] = useState<Channel[]>([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchChannels = async () => {
      try {
        const data = await fetchData("/channel/search?query="); // You can filter with query if needed
        setChannels(data.channels);
      } catch (err) {
        setError("Failed to load channels.");
      }
    };
    fetchChannels();
  }, []);

  return (
    <div className="bg-gray-900 text-white p-4 rounded-md">
      <h2 className="text-xl mb-4">Channels</h2>
      {error && <p className="text-red-500">{error}</p>}
      <ul>
        {channels.map((channel) => (
          <li key={channel.id} className="mb-2">
            <Link href={`/channel/${channel.id}`} className="text-blue-500 hover:underline">
              {channel.name}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ChannelList;
