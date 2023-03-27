export function Avatar({
  firstName,
  lastName,
  emailAddress,
}: {
  firstName?: string;
  lastName?: string;
  emailAddress?: string;
}) {
  let initials = emailAddress ? emailAddress.slice(0, 1).toUpperCase() : 'U';
  if (firstName && lastName) {
    initials = `${firstName.charAt(0).toUpperCase()}${lastName
      .charAt(0)
      .toUpperCase()}`;
  }
  return (
    <span className="inline-flex h-10 w-10 items-center justify-center rounded-full bg-orange-500 font-display">
      <span className="text-sm font-medium leading-none text-white">
        {initials}
      </span>
    </span>
  );
}
