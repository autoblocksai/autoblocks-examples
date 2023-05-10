import NextAuth from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';

export const authOptions = {
  theme: { colorScheme: 'dark' as 'dark', logo: '/images/logo.png' },
  providers: [
    CredentialsProvider({
      // The name to display on the sign in form (e.g. "Sign in with...")
      name: 'password',
      // `credentials` is used to generate a form on the sign in page.
      // You can specify which fields should be submitted, by adding keys to the `credentials` object.
      // e.g. domain, username, password, 2FA token, etc.
      // You can pass any HTML attribute to the <input> tag through the object.
      credentials: {
        password: { label: 'Docs Password', type: 'password' },
      },
      async authorize(credentials, req) {
        if (credentials && credentials.password === process.env.APP_PASSWORD) {
          return {
            id: 'autoblocks-user',
            name: 'Autoblocks User',
          };
        }

        return null;
      },
    }),
  ],
};
export default NextAuth(authOptions);
