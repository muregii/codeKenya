function strStr(haystack: string, needle: string): number {
  if (needle.length > haystack.length) return -1;
  return haystack.indexOf(needle);
}
