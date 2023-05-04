import type { NextApiRequest, NextApiResponse } from 'next';

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  await fetch('https://ingest-event.autoblocks.ai', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${process.env.AUTOBLOCKS_API_KEY}`,
    },
    body: req.body,
  });
  return res.status(200).json({});
}
