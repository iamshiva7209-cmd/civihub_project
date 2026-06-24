import React, { useEffect, useState } from 'react';

interface AnimatedHeadingProps {
  text: string;
  className?: string;
  initialDelay?: number;
  charDelay?: number;
  transitionDuration?: number;
}

export const AnimatedHeading: React.FC<AnimatedHeadingProps> = ({
  text,
  className = '',
  initialDelay = 200,
  charDelay = 30,
  transitionDuration = 500,
}) => {
  const [animate, setAnimate] = useState(false);
  const lines = text.split('\n');

  useEffect(() => {
    const timer = setTimeout(() => {
      setAnimate(true);
    }, initialDelay);

    return () => clearTimeout(timer);
  }, [initialDelay]);

  return (
    <h1
      className={`font-normal mb-4 ${className}`}
      style={{ letterSpacing: '-0.04em' }}
    >
      {lines.map((line, lineIndex) => {
        // Calculate delay parameters
        const lineLength = line.length;
        
        return (
          <div key={lineIndex} className="block whitespace-nowrap">
            {line.split('').map((char, charIndex) => {
              // Formula: (lineIndex * lineLength * charDelay) + (charIndex * charDelay)
              const tDelay = (lineIndex * lineLength * charDelay) + (charIndex * charDelay);
              const isSpace = char === ' ';

              return (
                <span
                  key={charIndex}
                  style={{
                    display: 'inline-block',
                    opacity: animate ? 1 : 0,
                    transform: animate ? 'translateX(0)' : 'translateX(-18px)',
                    transition: `opacity ${transitionDuration}ms cubic-bezier(0.16, 1, 0.3, 1), transform ${transitionDuration}ms cubic-bezier(0.16, 1, 0.3, 1)`,
                    transitionDelay: `${tDelay}ms`,
                  }}
                >
                  {isSpace ? '\u00A0' : char}
                </span>
              );
            })}
          </div>
        );
      })}
    </h1>
  );
};
