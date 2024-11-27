// utils/api.ts

export const fetchData = async (endpoint: string, options: RequestInit = {}): Promise<any> => {
  try {
    const res = await fetch(`http://localhost:5000${endpoint}`, options);
    if (!res.ok) {
      throw new Error('Failed to fetch data');
    }
    const data = await res.json();
    return data;
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};
