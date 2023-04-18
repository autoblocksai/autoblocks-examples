import NextAuth from 'next-auth';
import GoogleProvider from 'next-auth/providers/google';
import invariant from 'invariant';

invariant(process.env.GOOGLE_CLIENT_ID, 'No google client id');
invariant(process.env.GOOGLE_CLIENT_SECRET, 'No google client secret');

export const authOptions = {
  // Configure one or more authentication providers
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET,
    }),
  ],
  callbacks: {
    async signIn({ account, profile }: any) {
      if (account.provider === 'google') {
        return (
          profile.email_verified && profile.email.endsWith('@autoblocks.ai')
        );
      }
      return profile.email.endsWith('@autoblocks.ai'); // Do different verification for other providers that don't have `email_verified`
    },
  },
};
export default NextAuth(authOptions);
