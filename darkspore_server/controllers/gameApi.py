import time

class DarkSporeServerApi(object):
    def __init__(self, serverConfig, server):
        self.serverConfig = serverConfig
        self.server = server

    def api_getStatus_javascript(self, callback):
        javascript = ("var data = {status: {blaze: {health: 1}, gms: {health: 1}, nucleus: {health: 1}, game: {health: 1}}}; " +
                        "setTimeout(function(){" +

                            "oncriticalerror = false; " +
                            "setPlayButtonActive(); " +
                            "updateBottomleftProgressComment('DARKSPORE-LS ENABLED');" +
                            "updateProgressBar(1);" +
                            "document.getElementById('Patch_Content_Frame').style.display = 'block'; " +
                            "document.getElementById('ERROR_MESSAGE').style.height = '0px'; " +

                        "},200); " +
                        callback + ";")

        if self.serverConfig.shouldSkipLauncher():
            javascript = ("var data = {status: {blaze: {health: 1}, gms: {health: 1}, nucleus: {health: 1}, game: {health: 1}}}; "
                            "clickPlayButton();" +
                            "var runNow = function(){" +

                                "oncriticalerror = false; " +
                                "setPlayButtonActive(); " +
                                "updateBottomleftProgressComment('DARKSPORE-LS ENABLED');" +
                                "updateProgressBar(1);" +
                                "document.getElementById('Patch_Content_Frame').style.display = 'block'; " +
                                "document.getElementById('ERROR_MESSAGE').style.height = '0px'; " +

                                "clickPlayButton();" +
                                "setTimeout(runNow,1); " +
                            "}; " +
                            "runNow(); " +
                            callback + ";")
        return javascript

    def api_getStatus_object(self, include_broadcast):
        obj = {
                "status": {
                    "blaze":   {"health": 1},
                    "gms":     {"health": 1},
                    "nucleus": {"health": 1},
                    "game":    {"health": 1}
                }
              }

        if include_broadcast:
            obj.broadcast = []

        return obj

    def bootstrapApi_response_object(self, version):
        return {
                    "stat": 'ok',
                    "version": version,
                    "timestamp": str(long(time.time())),
                    "exectime": '1'
                }

    def bootstrapApi_getConfigs_object(self):
        return {
                    "blaze_service_name": 'darkspore',
                    "blaze_secure": 'N', # --CONFIRMED--
                    "blaze_env": 'production',
                    "sporenet_db_host": 'darkspore.com',
                    "sporenet_db_port": '80',
                    "sporenet_db_name": 'darkspore',
                    "sporenet_host": 'darkspore.com',
                    "sporenet_port": '80',
                    "liferay_host": 'darkspore.com',
                    "liferay_port": '80',
                    "launcher_action": '1', # --NUMBER--
                    "launcher_url": 'http://darkspore.com/bootstrap/launcher/notes'
                }

    def bootstrapApi_getAccount_object(self, id):
        print "Retrieving user info..."
        account = self.server.getAccount(id)
        return {
            "avatar_id": '1', # TODO
            "avatar_updated": '0', # Not sure of what is that
            "blaze_id": str(account.id),
            "chain_progression": str(account.chainProgression()),
            "creature_rewards": '0', # Not sure of what is that
            "current_game_id": '1', # Not sure of what is that
            "current_playgroup_id": '0', # Not sure of what is that
            "default_deck_pve_id": '1', # Not sure of what is that
            "default_deck_pvp_id": None, # Not sure of what is that
            "dna": '0', # TODO
            "email": account.email,
            "grant_online_access": '0', # Not sure of what is that
            "id": str(account.id),
            "level": str(account.level),
            "name": account.name,
            "new_player_inventory": '1', # Not sure of what is that
            "new_player_progress": '7000', # Not sure of what is that
            "nucleus_id": '1', # A different per-user ID (may be the same here?)
            "star_level": '0', # Not sure of what is that for, but it can't be 65536 or bigger
            "tutorial_completed": ('Y' if account.tutorialCompleted else 'N'),

            # catalysts are things you collect in game and make you stronger, and max amount of them is 9
            "unlock_catalysts": '0', # TODO
            "unlock_diagonal_catalysts": '0', # TODO

            # Editor flair is probably amount of "detail"  slots you can put on creature.
            "unlock_editor_flair_slots": '3', # TODO

            # Fuel might be: higher threat level unlock or amount of levels you can repeat after each one
            "unlock_fuel_tanks": '2', # TODO

            # Inventory is probably the amount of parts player can store.
            "unlock_inventory": '180', # TODO
            "unlock_inventory_identify": '0', # TODO

            "unlock_pve_decks": '1', # Not sure of what is that
            "unlock_pvp_decks": '0', # Not sure of what is that
            "unlock_stats": '0', # Not sure of what is that
            "xp": '201' # TODO
        }