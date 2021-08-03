import org.jetbrains.kotlin.gradle.tasks.KotlinCompile

plugins {
    kotlin("jvm") version "1.5.21"
    application
}

group = "me.home"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()

//    maven {setUrl("https://jitpack.io")  }
    // https://mvnrepository.com/artifact/org.mongodb/mongo-java-driver

}
dependencies {
//    compile 'com.github.carleslc:kotlin-extensions:0.7.6'
    implementation("org.mongodb:mongo-java-driver:3.12.9")
    implementation("org.pircbotx:pircbotx:2.1")
}


tasks.withType<KotlinCompile>() {
    kotlinOptions.jvmTarget = "1.8"
}

application {
    mainClassName = "MainKt"
}