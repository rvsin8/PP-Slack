// frontend/components/MessageInput.tsx
import { useState } from "react";
import { fetchData } from "../utils/api"; // Use your api function here to post messages

interface MessageInputProps {
  channelId: number; // This will be passed as prop to know which channel we are sending to
}

const MessageInput = ({ channelId }: MessageInputProps) => {
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!message.trim()) {
      setError("Message cannot be empty!");
      return;
    }

    try {
      // You will call your backend API for sending the message
      const data = await fetchData(`/message/channel/${channelId}/message`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ content: message }),
      });

      // Handle success (e.g., reset message input)
      if (data.message === "Message sent successfully") {
        setMessage(""); // Clear message input
      }
    } catch (err) {
      console.error(err);
      setError("Failed to send message. Please try again.");
    }
  };

  return (
    <div className="message-input-container p-4 bg-gray-800 rounded-md">
      <form onSubmit={handleSubmit} className="flex">
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type a message"
          className="w-full p-2 rounded-md"
        />
        <button type="submit" className="ml-2 bg-blue-500 text-white px-4 py-2 rounded-md">
          Send
        </button>
      </form>
      {error && <p className="text-red-500 mt-2">{error}</p>}
    </div>
  );
};

export default MessageInput;
