/* eslint-disable import/prefer-default-export */
export async function GET(req) {
  const { searchParams } = req.nextUrl;
  const query = searchParams.get('name');
  try {
    const personDNS = process.env.NEXT_PUBLIC_PERSON_DNS || '127.0.0.1';
    const response = await fetch(`http://${personDNS}:8001/persons/similar_search?name=${query}`);

    if (!response.ok) {
      return new Response('Error getting person data', {
        status: response.status,
      });
    }

    const data = await response.json();
    return Response.json(data);
  } catch (error) {
    return new Response(`Error: ${error.message}`, {
      status: 400,
    });
  }
}
