import { promises as fs } from 'fs';

export const handler = async (event) => {
  try {
    const htmlContent = await fs.readFile('HomePage.html', 'utf-8');

    const response = {
      statusCode: 200,
      headers: {
        'Content-Type': 'text/html',
      },
      body: htmlContent,
    };
    return response;
    
  } catch (error) {
    console.error('Error reading the HTML file:', error);

    const response = {
      statusCode: 500,
      body: JSON.stringify('Internal Server Error'),
    };

    return response;
  }
};
