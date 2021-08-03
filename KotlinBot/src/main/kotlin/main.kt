import com.mongodb.BasicDBObject
import com.mongodb.MongoClient
import com.mongodb.MongoException
import org.pircbotx.Configuration
import org.pircbotx.PircBotX
import org.pircbotx.hooks.ListenerAdapter
import org.pircbotx.hooks.types.GenericMessageEvent;

class MainKt : ListenerAdapter() {
override fun onGenericMessage(event: GenericMessageEvent) {
        //When someone says ?helloworld respond with "Hello World"
        if (event.getMessage().startsWith("?helloworld")) event.respond("Hello world!")
    }

    companion object {
        @Throws(Exception::class)
        @JvmStatic
        fun main(args: Array<String>) {
            //Configure what we want our bot to do
            val configuration: Configuration = Configuration.Builder()
                .setName("MangaBotKotlin") //Set the nick of the bot. CHANGE IN YOUR CODE
                .addServer("irc.libera.chat") //Join the freenode network
                .addAutoJoinChannel("#manga") //Join the official #pircbotx channel
                .addListener(MainKt()) //Add our listener that will be called on Events
                .buildConfiguration()

            //Create our bot with the configuration
            val bot = PircBotX(configuration)
            //Connect to the server
            bot.startBot()
        }
    }
}
//object MainKt {
//    @JvmStatic
//    fun main(args: Array<String>){
//        var bot
//        var mongoClient: MongoClient? = null
//        try {
//            mongoClient = MongoClient("127.0.0.1", 27017)
//            var db = mongoClient.getDB("testDB")
//            var tbl = db.getCollection("user")
//
//
//            val document = BasicDBObject()
//            document.put("name","dwane")
//            document.put("lastname","holmes")
//            tbl.insert(document)
//
//
//        } catch (e: MongoException) {
//            e.printStackTrace()
//        } finally {
//            mongoClient!!.close()
//        }
//    }
//
//    data class User(val name: String, val lastname: String)
//}