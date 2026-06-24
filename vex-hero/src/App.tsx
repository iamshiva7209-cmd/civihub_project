import { AnimatedHeading } from './components/AnimatedHeading';
import { FadeIn } from './components/FadeIn';

function App() {
  return (
    <div className="relative w-screen min-h-screen text-white overflow-hidden bg-black select-none">
      
      {/* BACKGROUND VIDEO (RAW, NO OVERLAYS) */}
      <video
        className="absolute top-0 left-0 w-full h-full object-cover z-0 pointer-events-none"
        src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260403_050628_c4e32401-fab4-4a27-b7a8-6e9291cd5959.mp4"
        autoPlay
        loop
        muted
        playsInline
      />

      {/* MAIN PAGE WRAPPER */}
      <div className="relative z-10 w-full min-h-screen flex flex-col justify-between">
        
        {/* NAVBAR */}
        <header className="w-full px-6 md:px-12 lg:px-16 pt-6">
          <div className="liquid-glass rounded-xl px-4 py-2 flex items-center justify-between">
            {/* Left: Logo */}
            <a href="/" className="text-2xl font-semibold tracking-tight text-white select-none">
              VEX
            </a>

            {/* Center: Links (Hidden on Mobile) */}
            <nav className="hidden md:flex items-center gap-8">
              <a href="#story" className="text-sm font-medium text-white/90 hover:text-gray-300 transition-colors">
                Story
              </a>
              <a href="#investing" className="text-sm font-medium text-white/90 hover:text-gray-300 transition-colors">
                Investing
              </a>
              <a href="#building" className="text-sm font-medium text-white/90 hover:text-gray-300 transition-colors">
                Building
              </a>
              <a href="#advisory" className="text-sm font-medium text-white/90 hover:text-gray-300 transition-colors">
                Advisory
              </a>
            </nav>

            {/* Right: Action Button */}
            <button 
              className="bg-white text-black px-6 py-2 rounded-lg text-sm font-medium hover:bg-gray-100 transition-all active:scale-[0.98]"
              onClick={() => alert('Start a Chat Clicked')}
            >
              Start a Chat
            </button>
          </div>
        </header>

        {/* HERO CONTENT (Pushed to bottom) */}
        <div className="w-full px-6 md:px-12 lg:px-16 pb-12 lg:pb-16 flex-1 flex flex-col justify-end">
          <div className="lg:grid lg:grid-cols-2 lg:items-end gap-12 lg:gap-8">
            
            {/* Left Column: Heading and Description */}
            <div>
              <AnimatedHeading 
                text={"Shaping tomorrow\nwith vision and action."} 
                className="text-4xl md:text-5xl lg:text-6xl xl:text-7xl leading-tight"
                initialDelay={200}
                charDelay={30}
              />

              <FadeIn delay={800} duration={1000}>
                <p className="text-base md:text-lg text-gray-300 mb-5 max-w-lg leading-relaxed">
                  We back visionaries and craft ventures that define what comes next.
                </p>
              </FadeIn>

              <FadeIn delay={1200} duration={1000}>
                <div className="flex flex-wrap gap-4">
                  <button 
                    className="bg-white text-black px-8 py-3 rounded-lg font-medium text-sm hover:bg-gray-100 transition-all active:scale-[0.98]"
                    onClick={() => alert('Start a Chat Clicked')}
                  >
                    Start a Chat
                  </button>
                  <button 
                    className="liquid-glass border border-white/20 text-white px-8 py-3 rounded-lg font-medium text-sm hover:bg-white hover:text-black transition-all active:scale-[0.98]"
                    onClick={() => alert('Explore Now Clicked')}
                  >
                    Explore Now
                  </button>
                </div>
              </FadeIn>
            </div>

            {/* Right Column: Glass Card Tag */}
            <div className="flex items-end justify-start lg:justify-end mt-8 lg:mt-0">
              <FadeIn delay={1400} duration={1000} className="w-full lg:w-auto">
                <div className="liquid-glass border border-white/20 px-6 py-3 rounded-xl w-full lg:w-auto text-center lg:text-left select-none">
                  <p className="text-lg md:text-xl lg:text-2xl font-light text-white tracking-wide">
                    Investing. Building. Advisory.
                  </p>
                </div>
              </FadeIn>
            </div>

          </div>
        </div>

      </div>

    </div>
  );
}

export default App;
