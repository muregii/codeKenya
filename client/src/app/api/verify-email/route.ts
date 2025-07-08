import { NextResponse } from "next/server";

export async function POST(request: Request) {
  const { email } = await request.json();
  const apiKey = process.env.NEXT_PUBLIC_QUICK_EMAIL_VERIFICATION_API_KEY;

  try {
    const response = await fetch(
      `https://api.quickemailverification.com/v1/verify?email=${encodeURIComponent(
        email
      )}&apikey=${apiKey}`
    );

    if (!response.ok) {
      throw new Error(`API request failed with status ${response.status}`);
    }

    const data = await response.json();
    return NextResponse.json(data);
  } catch (error) {
    console.error("Email verification error:", error);
    return NextResponse.json(
      {
        success: false,
        message: "Email verification service unavailable",
        error: error instanceof Error ? error.message : "Unknown error",
      },
      { status: 500 }
    );
  }
}
