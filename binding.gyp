{
  'targets': [
    {
      'target_name': 'binding',
      'sources': [ './src/fb-bindings.cc', './src/fb-bindings-blob.cc',
                   './src/fb-bindings-fbresult.cc',
                   './src/fb-bindings-connection.cc','./src/fb-bindings-eventblock.cc',
                   './src/fb-bindings-fbeventemitter.cc', 
                   './src/fb-bindings-statement.cc' ],
      'include_dirs': [
          '<(module_root_dir)/fb/include'
      ],
      "conditions" : [
            [
                'OS=="linux"', {
                    'libraries': [ '-lfbclient' ]
                }
            ],
            [
                'OS=="win"', {
                  "libraries" : [
                      '<(module_root_dir)/fb/lib/fbclient_ms.lib'
                  ]
                }
            ]
      ]
    }
  ]
}
