export { default } from 'next-auth/middleware';

export const config = {
  matcher: ['/((?!images|favicon.ico).*)'],
};
