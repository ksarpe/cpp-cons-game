workspace "cppGame"
    architecture "x64"

    configurations
    {
        "Debug",
        "Release",
        "Dist"
    }

outputdir = "%{cfg.buildcfg}-%{cfg.system}-%{cfg.architecture}"

-- Project Player
project "Player"
    location "Player"
    kind "ConsoleApp"
    language "C++"

    targetdir ("bin/" .. outputdir .. "/%{prj.name}")
    objdir ("bin-int/" .. outputdir .. "/%{prj.name}")

    files
    {
        "%{prj.name}/include/**.h",
        "%{prj.name}/src/**.cpp",
        "%{prj.name}/main.cpp"
    }

    includedirs
    {
        "%{prj.name}/include"
    }

    filter "system:windows"
        cppdialect "C++17"
        systemversion "latest"       
    
    filter "configurations:Debug"
        defines "CG_DEBUG"
        symbols "On"
    
    filter "configurations:Release"
        defines "CG_RELEASE"
        optimize "On"
    
    filter "configurations:Dist"
        defines "CG_DIST"
        optimize "On"

