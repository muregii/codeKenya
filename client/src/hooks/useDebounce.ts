import { useCallback, useRef } from "react";

type DebouncedFunction<T extends (...args: unknown[]) => unknown> = {
  (...args: Parameters<T>): void;
  flush: () => void;
  cancel: () => void;
};

const useDebounce = <T extends (...args: unknown[]) => ReturnType<T>>(
  callback: T,
  delay: number
): DebouncedFunction<T> => {
  const timer = useRef<NodeJS.Timeout>();
  const callbackRef = useRef(callback);
  const pendingArgsRef = useRef<Parameters<T>>();

  // Update the callback if it changes
  callbackRef.current = callback;

  const debouncedFunction = useCallback(
    (...args: Parameters<T>) => {
      pendingArgsRef.current = args;
      clearTimeout(timer.current);
      timer.current = setTimeout(() => {
        callbackRef.current(...args);
        pendingArgsRef.current = undefined;
      }, delay);
    },
    [delay]
  ) as DebouncedFunction<T>;

  // Add flush method to immediately invoke pending calls
  debouncedFunction.flush = () => {
    clearTimeout(timer.current);
    if (pendingArgsRef.current) {
      callbackRef.current(...pendingArgsRef.current);
      pendingArgsRef.current = undefined;
    }
  };

  // Add cancel method to cancel pending calls
  debouncedFunction.cancel = () => {
    clearTimeout(timer.current);
    pendingArgsRef.current = undefined;
  };

  return debouncedFunction;
};

export default useDebounce;
