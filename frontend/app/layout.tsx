import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";  // Global styles for the whole app

// Custom fonts
const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

// Metadata for the app
export const metadata: Metadata = {
  title: "Slack Clone",  // Updated title
  description: "A clone of Slack with messaging features",  // Updated description
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <head>
        {/* Here you can add your app's meta tags like favicon, theme color, etc */}
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </head>
      <body className={`${geistSans.variable} ${geistMono.variable} antialiased`}>
        <header>
          <h1>Slack Clone</h1>
          {/* You can add navigation here */}
        </header>

        <main>{children}</main>

        <footer>
          {/* Global footer */}
          <p>&copy; 2024 Slack Clone</p>
        </footer>
      </body>
    </html>
  );
}
