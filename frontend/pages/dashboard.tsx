// frontend/pages/dashboard.tsx
import ChannelList from "../components/ChannelList";
import DMList from "../components/DMList";
import MessageInput from "../components/MessageInput";

const Dashboard = () => {
  return (
    <div className="container mx-auto p-8">
      <h1 className="text-3xl font-bold mb-8">Welcome to Slack Clone Dashboard</h1>
      <div className="flex gap-8">
        <div className="w-1/3">
          <ChannelList />
        </div>
        <div className="w-1/3">
          <DMList />
        </div>
        <div className="w-1/3">
          <MessageInput channelId={1} /> {/* Pass selected channel ID here */}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
